import spacy
import pprint
import datetime

NLP = spacy.load('en_core_web_sm')
pretty_printer = pprint.PrettyPrinter(indent=4)

def processTranscript(transcript):
    meetings = []
    tasks = []
    doc = NLP(transcript)
    for sentence in doc.sents:
        # Try to extract meeting from a sentence
        meeting = getMeetingFromSentence(sentence)
        if meeting != {}:
            meetings.append(meeting)
            continue

        # If there is no meetings, try to extract a task from the sentence
        task = getTaskFromSentence(sentence)
        if task != {}:
            tasks.append(task)
            continue

    pretty_printer.pprint(meetings)
    pretty_printer.pprint(tasks)
    return meetings, tasks

def getMeetingFromSentence(sentence):
    if 'schedule' in sentence.text or 'sync' in sentence.text:
        currentMeeting = {}
        for token in sentence:
            if (token.dep_ == 'nsubj' or token.dep_ == 'relcl') and token.pos_ == 'PROPN':
                currentMeeting['Organiser'] = token.text
        
        sentenceDoc = NLP(sentence.text)
        for entity in sentenceDoc.ents:
            if entity.label_ == 'PERSON':
                if not 'Participants' in currentMeeting:
                    currentMeeting['Participants'] = []
                currentMeeting['Participants'].append(entity.text)
            
            if entity.label_ == 'DATE':
                currentMeeting['Time'] = entity.text
                currentMeeting['TimeRelativeTo'] = datetime.date.today()
        
        return currentMeeting
    else:
        return {}



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


testTranscript = u'Abhirup will be doing the integration. Abhirup has a ball as well. Steve will schedule a meeting with David and Jim tomorrow. Justin to sync with Mike by Friday. Sanket has the task of client UI. Rishabh will own the backend.'

if __name__ == "__main__":
    processTranscript(testTranscript)
