import os
import numpy as np
from yattag import Doc
import matplotlib.pyplot as plt
import re
import graphviz
import glob


# TODO: write doc, include that you need to install yattag


class Visual:

    def __init__(self, d, c, e, code):
        self.D = d
        self.C = c
        self.IdMap = {'Ambiguous': 'Ambiguous',
                      '<class \'list\'>': 'List',
                      '<class \'float\'>': 'Float',
                      '<class \'str\'>': 'String',
                      '<class \'int\'>': 'Integer',
                      '<class \'tuple\'>': 'Tuple',
                      '<class \'bool\'>': 'Boolean',
                      '<class \'set\'>': 'Set',
                      '<class \'dict\'>': 'Dictionary',
                      'Error': 'Error',
                      'Multiple': 'Multiple'
                      }
        self.errorMap = e
        self.code = code

    def generateReports(self):
        htmlText = self.generateHighlightedCode(self.C['Default'], self.code.split('\n'))
        errorText = self.generateErrorReport(self.C['Default'], self.code.split('\n'))

        with open("../output/error_report/ErrorReport.html", "w") as file1:
            file1.writelines(errorText)

        with open("../output/analysis/analysis.html", "w") as file1:
            file1.writelines(htmlText)

        # self.createGraphs(lifetimeVariableMap)

        self.createFlowChart()
        self.groupPages()

    def groupFlowchart(self):
        doc, tag, text = Doc().tagtext()

        with tag('html'):
            with tag('head'):
                doc.stag('link', rel='stylesheet', href='flow.css')
            with tag('body'):
                files = glob.glob('../output/flowchart/*')
                for f in files:
                    if f.title().split(".")[-1] == "Html":
                        link = f.title().split("/")[-1].lower()
                        link = '../' + re.sub(r'\\', '/', link)

                        with tag('div', klass='parent'):
                            with tag('h2'):
                                with tag('a', href=link, klass='b1'):
                                    temp_name = f.title().split("\\")[-1].split('.')[0]
                                    temp_name = temp_name.replace(temp_name.split('_')[0] + '_', '')
                                    text(temp_name.lower())

        result = doc.getvalue()

        with open(f"../output/flowchartgroup/flow.html", "w") as file1:
            file1.writelines(result)

    def groupPages(self):
        self.groupFlowchart()

        doc, tag, text = Doc().tagtext()

        with tag('html'):
            with tag('head'):
                doc.stag('link', rel='stylesheet', href='Main.css')
            with tag('body'):
                doc.stag('br')
                with tag('h1', klass='h1'):
                    text("Python Type Static Analysis Tool")
                doc.stag('br')
                with tag('div', klass='parent'):
                    with tag('h2'):
                        with tag('a', href='analysis/analysis.html', klass='b1'):
                            text("Type Analysis Highlighting")
                with tag('div', klass='parent'):
                    with tag('h2'):
                        with tag('a', href='flowchartgroup/flow.html', klass='b2'):
                            text("Type History Flowcharts")
                with tag('div', klass='parent'):
                    with tag('h2'):
                        with tag('a', href='error_report/ErrorReport.html', klass='b3'):
                            text("Error Report Summary")

        result = doc.getvalue()

        with open(f"../output/Main.html", "w") as file1:
            file1.writelines(result)

    def createFlowChart(self):
        files = glob.glob('../output/flowchart/*')
        for f in files:
            os.remove(f)

        for fn in self.D:
            lfn = []
            fn_s = fn.split("|")[0]
            fn_i = int(fn.split("|")[1])
            param = ''
            for i in range(fn_i + 1):
                param += ('arg' + str(i) + ',')

            fn_new = fn_s + '(' + param[0:(len(param) - 1)] + ')'
            for var in self.D[fn]:
                prev = None
                g = graphviz.Digraph(filename=f'../output/flowchart/flowchart_{fn_new}_{var}.gv', format='svg')
                lfn.append(f'../output/flowchart/flowchart_{fn_new}_{var}.gv.svg')
                if var == 'return':
                    g.attr(label=f'Return Type')
                else:
                    g.attr(label=f'Variable <{var}>')
                g.attr(bgcolor="#f5f2f0")
                g.attr('node', shape='box')
                g.attr('node', fontname="Consolas,Monaco,'Andale Mono','Ubuntu Mono',monospace")
                g.attr(fontname="Consolas,Monaco,'Andale Mono','Ubuntu Mono',monospace")

                for ln_no in self.D[fn][var]:
                    if ln_no < 0:
                        new_ln_no = "arg" + str(np.abs(ln_no) - 1)
                    else:
                        new_ln_no = str(ln_no)
                    tp_s = []
                    if isinstance(self.D[fn][var][ln_no], set):
                        for tp in self.D[fn][var][ln_no]:
                            tp_s.append(self.IdMap[str(tp)])
                    else:
                        tp_s.append(self.D[fn][var][ln_no])

                    g.node(str(ln_no), " " + new_ln_no + ": " + re.sub('\[|\]|\'', '', str(tp_s)) + " ")
                    if prev is not None:
                        g.edge(prev, str(ln_no))
                    prev = str(ln_no)

                g.render()

            for i in range(len(lfn)):
                lfn[i] = re.sub('../output/flowchart/', '', lfn[i])

            doc, tag, text = Doc().tagtext()

            with tag('html'):
                with tag('head'):
                    doc.stag('link', rel='stylesheet', href='../flowchartcss/flowchart.css')
                    # with tag('script'):
                    #     doc.attr(src='../flowchartcss/flowchart.js')
                with tag('body'):
                    with tag('h1', klass='h1'):
                        text("Function " + fn_new + " Type History")
                    doc.stag('hr')
                    for fn in lfn:
                        doc.stag('br')
                        with tag('object', type='image/svg+xml', data=fn, klass='center'):
                            doc.stag('img', src=fn, klass='center')
                        # with tag('iframe', klass='center', width='0', height='0', frameBorder='0', src=fn,
                        #          onload='resize(this)'):
                        #     text('')
                        doc.stag('br')
                        doc.stag('hr')

            result = doc.getvalue()

            with open(f"../output/flowchart/flowchart_{fn_new}.html", "w") as file1:
                file1.writelines(result)

    def generateHighlightedCode(self, typeMapping, codeList):
        doc, tag, text, line = Doc().ttl()
        lifetimeVariableMap = {}
        with tag('html'):
            with tag('head'):
                doc.stag('link', rel='stylesheet', href='analysis.css')
                doc.stag('link', rel='stylesheet', href='prism.css')
            with tag('body', klass='line-numbers'):
                with tag('script'):
                    doc.attr(src='prism.js')
                self.highlightCodeLines(typeMapping, codeList, lifetimeVariableMap, doc, tag, text)
                with tag('ul', klass='legend'):
                    for key in self.IdMap:
                        with tag('li'):
                            line('span', '', klass=self.IdMap[key])
                            text(self.IdMap[key])

        return doc.getvalue()

    def highlightCodeLines(self, typeMapping, codeList, lifetimeVariableMap, doc, tag, text):
        functionTypeMap = {}
        lineNumber = 1
        functionName = ''
        functionVariableMap = {}
        with tag('pre'):
            with tag('code', klass='language-python'):
                for code in codeList:
                    codeSplit = code.split()
                    if (len(codeSplit) > 0 and codeSplit[0] == 'def'):
                        functionName = codeSplit[1].split('(')[0]
                        numParameters = self.getNumParameters(code)
                        key = functionName + '|' + str(numParameters)
                        functionTypeMap = typeMapping[key]
                        functionVariableMap = {}

                        if ('return' in typeMapping[key]):
                            returnType = list(typeMapping[key]['return'].values())[0]

                            tagID = self.getClassIdFromType(returnType)
                            if (tagID == "Multiple"):
                                with tag('div', klass='tooltip'):
                                    with tag('mark', klass=tagID):
                                        text(code)
                                    with tag('span', klass='tooltiptext'):
                                        tooltipList = ''
                                        for varType in returnType:
                                            tooltipList = f'{tooltipList} {self.IdMap[str(varType)]}, '
                                        text(f'{tooltipList[:-2]} ')
                            else:
                                with tag('mark', klass=tagID):
                                    text(code)
                        else:
                            text(code)
                    elif len(codeSplit) > 0 and codeSplit[0] == '#':
                        text(f'{code}\n')
                        lineNumber += 1
                        continue
                    else:
                        self.extractVariablesFromLine(code, functionTypeMap, lineNumber, functionVariableMap, doc, tag,
                                                      text)
                        lifetimeVariableMap[functionName] = functionVariableMap
                    lineNumber += 1
                    text('\n')

    # get all variables that exist in map and their indicies
    def extractVariablesFromLine(self, codeLine, typeMap, lineNumber, functionVariableMap, doc, tag, text):
        printed = False
        for key in typeMap:
            if (lineNumber in typeMap[key]):
                typeOfVar = typeMap[key][lineNumber]
                codeSplitByEqual = codeLine.split('=')

                if (len(codeSplitByEqual) > 1):
                    index = 0
                    if len(codeSplitByEqual) > 2:
                        new_split = []
                        for var in codeSplitByEqual:
                            new_split.append(re.sub(' ', '', var))
                        for i, var in enumerate(new_split):
                            if key == var:
                                index = i

                    printed = True
                    classId = self.getClassIdFromType(typeOfVar)
                    locVar = codeSplitByEqual[index].index(key)
                    variableName = codeSplitByEqual[index][locVar:locVar + len(key)]
                    if (variableName in functionVariableMap):
                        functionVariableMap[variableName].append((lineNumber, typeOfVar))
                    else:
                        functionVariableMap[variableName] = [(lineNumber, typeOfVar)]
                    text(codeSplitByEqual[index][0:locVar])
                    if (classId == "Multiple"):
                        with tag('div', klass='tooltip'):
                            with tag('mark', klass=classId):
                                text(variableName)
                            if len(codeSplitByEqual) > 2:
                                if index == len(codeSplitByEqual) - 2:
                                    text(f'{codeSplitByEqual[index][locVar + len(key):]}={codeSplitByEqual[index + 1]}')
                                    with tag('span', klass='tooltiptext'):
                                        tooltipList = ''
                                        for varType in typeOfVar:
                                            tooltipList = f'{tooltipList} {self.IdMap[str(varType)]}, '
                                        text(f'{tooltipList[:-2]} ')
                                else:
                                    text(f' =')
                                    with tag('span', klass='tooltiptext'):
                                        tooltipList = ''
                                        for varType in typeOfVar:
                                            tooltipList = f'{tooltipList} {self.IdMap[str(varType)]}, '
                                        text(f'{tooltipList[:-2]} ')
                            else:
                                text(f'{codeSplitByEqual[index][locVar + len(key):]}={codeSplitByEqual[1]}')
                                with tag('span', klass='tooltiptext'):
                                    tooltipList = ''
                                    for varType in typeOfVar:
                                        tooltipList = f'{tooltipList} {self.IdMap[str(varType)]}, '
                                    text(f'{tooltipList[:-2]} ')
                    else:
                        with tag('mark', klass=classId):
                            text(variableName)
                        if len(codeSplitByEqual) > 2:
                            if index == len(codeSplitByEqual) - 2:
                                text(f'{codeSplitByEqual[index][locVar + len(key):]}={codeSplitByEqual[index + 1]}')
                            else:
                                text(f' =')
                        else:
                            text(f'{codeSplitByEqual[index][locVar + len(key):]}={codeSplitByEqual[1]}')
        if printed is False:
            text(codeLine)

    def getClassIdFromType(self, typeOfVar):
        if isinstance(typeOfVar, set):
            if (len(typeOfVar) == 1):
                return self.IdMap[str(next(iter(typeOfVar)))]
            else:
                return "Multiple"
        elif isinstance(typeOfVar, str):
            return self.IdMap[typeOfVar]

    def getNumParameters(self, codeSplit):
        methodName = codeSplit.split(" ", 1)[1]
        methodName = re.sub('\ ', '', methodName)
        if (len(methodName.split("(")[1]) == 2):
            return 0
        if (len(methodName.split(",")) == 1):
            return 1
        return len(methodName.split(","))

    def createGraphs(self, lifetimeVariableMap):
        files = glob.glob('../output/type_history_scatter/*')
        for f in files:
            os.remove(f)

        for key in lifetimeVariableMap:
            methodVariables = lifetimeVariableMap[key]
            for variable in methodVariables:
                variableList = methodVariables[variable]
                lineNums = []
                typeVars = []
                y = list(self.IdMap.values())
                for tpl in variableList:
                    typeVars.append(y.index(self.getClassIdFromType(tpl[1])))
                    lineNums.append(tpl[0])
                # print(typeVars)
                fig, ax = plt.subplots(1, 1)
                ax.set_yticks(range(0, len(y)))
                ax.set_yticklabels(y)
                plt.title('Type History of Variable ' + '<' + variable + '>' + ' in method ' + key)
                plt.xlabel('Line Numbers')
                plt.ylabel('Type')

                plt.plot(lineNums, typeVars, '.')
                plt.savefig(f'../output/type_history_scatter/typeHistory-method-{key}-{variable}.png',
                            bbox_inches='tight')

    def generateErrorReport(self, typeMapping, codeList):
        doc, tag, text = Doc().tagtext()
        with tag('html'):
            with tag('head'):
                doc.stag('link', rel='stylesheet', href='ErrorReport.css')
        with tag('body'):
            self.generateErrors(typeMapping, codeList, doc, tag, text)
        return doc.getvalue()

    def generateErrors(self, typeMapping, codeList, doc, tag, text):
        functionTypeMap = {}
        lineNumber = 1
        with tag('code'):
            with tag('h1'):
                text("Error Log")
            for code in codeList:
                codeSplit = code.split()
                if (len(codeSplit) > 0 and codeSplit[0] == 'def'):
                    functionName = codeSplit[1].split('(')[0]
                    numParameters = self.getNumParameters(code)
                    key = functionName + '|' + str(numParameters)
                    functionTypeMap = typeMapping[key]
                elif len(codeSplit) > 0 and codeSplit[0] == '#':
                    lineNumber += 1
                    continue
                else:
                    self.getErrorLineFromCode(code, functionTypeMap, lineNumber, doc, tag, text)
                lineNumber += 1
            for key in sorted(self.errorMap):
                with tag('p'):
                    text(f"{str(key)}: {self.errorMap[key].lower()}")

    def getErrorLineFromCode(self, code, typeMap, lineNumber, doc, tag, text):
        printed = False
        for key in typeMap:
            if (lineNumber in typeMap[key]):
                typeOfVar = typeMap[key][lineNumber]
                codeSplitByEqual = code.split('=')
                if (len(codeSplitByEqual) == 2):
                    printed = True
                    classId = self.getClassIdFromType(typeOfVar)
                    with tag('p', klass=classId):
                        locVar = codeSplitByEqual[0].index(key)
                        # text(codeSplitByEqual[0][0:locVar])
                        # with tag('mark'):
                        # text(codeSplitByEqual[0][locVar:locVar+len(key)])
                        # text(f'{codeSplitByEqual[0][locVar+len(key):]}={codeSplitByEqual[1]}')
                        if (typeOfVar == 'Ambiguous') and lineNumber not in self.errorMap:
                            self.errorMap[
                                lineNumber] = 'Warning, there may be any error on this line due to the ambigious nature of the variables'
                        if (typeOfVar == 'Error') and lineNumber not in self.errorMap:
                            self.errorMap[lineNumber] = 'Error, there is an error on this line caused by type mismatch'
        # if printed is False:
        # with tag('p'):
        # text(code)
        # TODO: support multiple
        # TODO: hover functionality if multiple types
