import spacy
import pprint
import datetime

DAY_LIST = ['today', 'tomorrow', 'yesterday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'month', 'day', 'week']

def sbd_component(doc):
    for i, token in enumerate(doc[:-1]):
        # define sentence start if period + titlecase token
        if token.text in DAY_LIST:
            doc[i + 1].sent_start = True
    return doc

NLP = spacy.load('en_core_web_sm')
NLP.add_pipe(sbd_component, before='parser')
pretty_printer = pprint.PrettyPrinter(indent=4)


def processTranscript(transcript):
    print("transcript: ", transcript)
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
    if 'schedule' in sentence.text or 'sync' in sentence.text or 'meeting' in sentence.text:
        currentMeeting = {}
        for token in sentence:
            if (token.dep_ == 'nsubj' or token.dep_ == 'relcl') and token.pos_ == 'PROPN':
                currentMeeting['Organiser'] = token.text
                currentMeeting['Participants'] = [token.text]

        sentenceDoc = NLP(sentence.text)
        for entity in sentenceDoc.ents:
            if entity.label_ == 'PERSON':
                if not 'Participants' in currentMeeting:
                    currentMeeting['Participants'] = []
                if entity.text not in currentMeeting['Participants']:
                    currentMeeting['Participants'].append(entity.text)

            if entity.label_ == 'DATE':
                currentMeeting['Time'] = entity.text

        return currentMeeting
    else:
        return {}


def getTaskFromSentence(sentence):
    if 'will' in sentence.text or 'task' in sentence.text or 'going to' in sentence.text:
        currentTask = {}
        for token in sentence:
            if token.dep_ == 'nsubj' and token.pos_ == 'PROPN':
                currentTask['Person'] = token.text

            if token.dep_ == 'dobj' and token.text != 'task':
                currentTask['Task'] = ' '.join(str(x) for x in token.subtree)

        if not 'Task' in currentTask:
            for token in sentence:
                if token.dep_ == 'pobj':
                    currentTask['Task'] = ' '.join(
                        str(x) for x in list(token.ancestors)[0].subtree)

        if 'Person' in currentTask and 'Task' in currentTask:
            taskDoc = NLP(currentTask['Task'])
            i = 0
            for token in taskDoc:
                if token.text == 'the' or token.text == 'of':
                    i += 1
                else:
                    break

            currentTask['Task'] = taskDoc[i:].text
            return currentTask
        else:
            return {}
    else:
        return {}



testTranscript =  u'Abhirup will be doing the integration of backend and frontend. Abhirup has a ball as well. Steve will schedule a meeting with David and Jim tomorrow. Justin to sync with Mike by tomorrow Sanket has the task of client UI. Rishabh will own the backend and the unit tests. David will complete the back end unit tests.'

if __name__ == "__main__":
    processTranscript(testTranscript)
