print("\n\nPenOS!\n")
print("Welcome To PenOS,")
print("a open-source Command Line Interface For Launching And Developing Applications")
print("------------------------------------------------------------------------------")
print("Type run To Run A Module.")
    
print('\n If You Want You Can Create Modules. Go To penshellpenos.web.app for more info')
print("                             Starting PenOS...")
print("------------------------------------------------------------------------\n\n")
    
while True:
    command = input("====>")
    if command == "run":
        pname = input("Package's Name: ")
        filename = "Core/PenOS/Modules/" + pname + '/' + pname + '.py'
        exec(open(filename).read())
        print("Package Execution Over, You are Back...")
    if command == "pencode":   
        def pencode(inputs):
            print("running: " + inputs)
            tmp = []
            tid = ''
            tokens = []
            keywords = [
                'penOut',
                'penGo',
                'penStop',
                'penIn'
            ]

            for l in inputs:
                if l == '"' and tid == '':
                    tid = "char"
                    tmp = []
                elif l == '"' and tid == 'char':
                    tokens.append({'id': tid, 'value': ''.join(tmp)})
                    tid = ''
                    tmp = []
                elif l == '\n':
                    if len(tmp) > 0:
                        tokens.append({'id': 'atom', 'value': ''.join(tmp)})
                        tmp = []
                elif l == ':':
                    tokens.append({'id': 'label', 'value': ''.join(tmp)})
                    tmp = []
                elif ''.join(tmp) in keywords:
                    tokens.append({'id': 'keyword', 'value': ''.join(tmp)})
                    tmp = []
                elif (l == ' ' or l == '\t') and tid != 'char':
                    continue
                elif l == '/' and tid == '':
                    tid = "comment"
                    tmp = []
                elif l == '/' and tid == 'comment':
                    tokens.append({'id': tid, 'value': ''.join(tmp)})
                    tid = ''
                    tmp = []
                else:
                    tmp.append(l)
            AST = []
            def add_node(parent, node):
                for a in AST:
                    if parent in a:
                        a[parent].append(node)

            def ignore():
                for token in tokens:
                    quit()
            
            saved = {}
            parent = {}
            collect = False

            for token in tokens:
                if token['id'] == 'label':
                    t = {token['value']: []}

                    if parent != t:
                        parent = token['value']
                        AST.append(t)
                
                elif token['id'] == 'keyword':
                    if token['value'] == 'stop':
                        t = {token['value']: 0}
                        add_node(parent, t)

                    else:
                        if collect == False:
                            saved = token
                            collect = True
                        else:
                            t = {saved['value']: token['value']}
                            add_node(parent, t)
                            collect = False
                elif token['id'] == 'char' or token['id'] == 'atom':
                    if collect == False:
                        saved = token
                        collect = True
                    else:
                        t = {saved['value']: token['value']}
                        add_node(parent, t)
                        collect = False
                
                elif token['id'] == 'comment':
                    ignore()

            def run(node):
                if isinstance(node, list):
                    for n in node:
                        for k, v in iter(n.items()):
                            execute([k, v])

                elif isinstance(node, dict):
                    for k, v in node.iteritems():
                        execute([k, v])

            def execute(loc):
                if isinstance(loc[1], list):
                    run(loc[1])
                elif loc[0] == 'penOut':
                    giveout(loc[1])      
                elif loc[0] == 'penStop':
                    stop()
                elif loc[0] == 'penGo':
                    goto(loc[1])
                elif loc[0] == 'penIn':
                    penIn(loc[1])

            def goto(v):
                for node in AST:
                    if v in node:
                        run(node[v])
            
            def penIn(v):
                    userinput = input("looks like you program needs input: ")
                    print(userinput)
            
            def giveout(v):
                print(v)  

            def stop():
                quit()

            
        print("Pencode Next v1.0.0")
        print("WARN: Pencode Next is depricated, please switch to builderlang.")
        todo = input(">>> ")
        pencode(todo)
        print('sorry, compiler isnt aviliable.')
    elif command == "quit":
        break
