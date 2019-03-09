import spacy
import pprint

NLP = spacy.load('en_core_web_sm')
pretty_printer = pprint.PrettyPrinter(indent=4)

def getTasksFromTranscript(transcript):
    tasks = []
    doc = NLP(transcript)
    for sentence in doc.sents:
        task = getTaskFromSentence(sentence)
        if 'Person' not in task or 'Task' not in task:
            continue
        tasks.append(getTaskFromSentence(sentence))
    
    pretty_printer.pprint(tasks)

def getTaskFromSentence(sentence):
    if 'will' in sentence.text or 'task' in sentence.text:
        currentTask = {}
        for token in sentence:
            if token.dep_ == 'nsubj' and token.pos_ == 'PROPN':
                currentTask['Person'] = token.text

            if token.dep_ == 'pobj' and (token.pos_ == 'NOUN' or token.pos_ == 'PROPN'):
                currentTask['Task'] = {
                    'Text': token.text,
                    'Type': token.dep_
                }
            
            if token.dep_ == 'dobj' and (token.pos_ == 'NOUN' or token.pos_ == 'PROPN') and not 'Task' in currentTask:
                currentTask['Task'] = {
                    'Text': token.text,
                    'Type': token.dep_
                }
        
        if 'Person' in currentTask and 'Task' in currentTask:
            currentTask['Task'] = currentTask['Task']['Text']
            return currentTask
        else:
            return {}
    else:
        return {}


testTranscript = u'Abhirup will be doing the integration. Abhirup has a ball as well. Sanket has the task of client UI. Rishabh will own the backend.'

getTasksFromTranscript(testTranscript)
