import time
from queue import Queue, Empty
from threading import *

class Event:
    """event"""
    def __init__(self, type_=None):
        self.type_ = type_      # Event type
        self.dict = {}          # Dictionaries are used to store specific event data


class EventManager:
    """Event manager"""
    def __init__(self):
        # The list of event objects can use queues or lists
        self.__eventQueue = Queue()
        # Event manager switch
        self.__active = False
        # Event processing thread
        self.__thread = Thread(target=self.__run)
        # The count variable is used to observe the order of execution
        self.count = 0
        # Here__ The handler is a dictionary, which is used to save the response function of the corresponding event. The value corresponding to each key is a list, in which the response function listening to the event is saved, one to many
        self.__handlers = {}

    def __run(self):
        print('{}_run'.format(self.count))
        while self.__active is True:
            try:
                event = self.__eventQueue.get(block=True, timeout=1)
                self.__event_process(event)
            except Empty:
                pass
            self.count += 1

    def __event_process(self, event):
        """The registered callbacks are executed in turn"""
        print('{}_EventProcess'.format(self.count))
        # Check if there is a handler to listen to the event
        if event.type_ in self.__handlers:
            # If it exists, events are passed to the handler function in order to execute
            for handler in self.__handlers[event.type_]:
                handler(event)
        self.count += 1

    def start(self):
        print('{}_Start'.format(self.count))
        # Set event manager to start
        self.__active = True
        # Start event processing thread
        self.__thread.start()
        self.count += 1

    def stop(self):
        """stop it"""
        print('{}_Stop'.format(self.count))
        # Set event manager to stop
        self.__active = False
        # Wait for the event processing thread to exit
        self.__thread.join()
        self.count += 1

    def add_event_listener(self, type_, handler):
        """Binding events and listener handling functions"""
        print('{}_AddEventListener'.format(self.count))

        # Try to get the list of processing functions corresponding to the event type, or create if none
        try:
            handlerList = self.__handlers[type_]
        except KeyError:
            handlerList = []

        self.__handlers[type_] = handlerList
        # If the processor you want to register is not in the list of processors for the event, register the event
        if handler not in handlerList:
            handlerList.append(handler)
        print(self.__handlers)
        self.count += 1

    def remove_event_listener(self, type_, handler):
        """Remove handler for listener"""
        print('{}_RemoveEventListener'.format(self.count))
        try:
            handlerList = self.__handlers[type_]
            # If the function exists in the list, it is removed
            if handler in handlerList:
                handlerList.remove(handler)
            # If the function list is empty, the event type is removed from the engine
            if not handlerList:
                del self.__handlers[type_]
        except KeyError:
            pass
        self.count += 1

    def send_event(self, event):
        """Putting events into the queue """
        print('{}_SendEvent'.format(self.count))
        self.__eventQueue.put(event)
        self.count += 1


# Time name new article
EVENT_ARTICAL = "Event_Artical"


# Official account of event source
class PublicAccounts:
    def __init__(self, eventManager):
        self.__eventManager = eventManager

    def write_newartical(self):
        # The event object wrote a new article
        event = Event(type_=EVENT_ARTICAL)
        # event data 
        event.dict["artical"] = u'How to write more elegant code\n'
        # Send event
        self.__eventManager.send_event(event)
        print(u'The official account sends new articles.\n')


class Listener:
    # Listener subscriber
    def __init__(self, username):
        self.__username = username

    def read_artical(self, event):
        # The processing function of the listener reads the article
        print(u'%s New article received' % self.__username)
        print(u'Reading new article:%s' % event.dict["artical"])


def have_a_test():
    # Instantiation listener
    listner1 = Listener("thinkroom")  # Subscriber 1
    listner2 = Listener("steve")      # Subscriber 2

    # Instantiating event operation function
    event_manager = EventManager()

    # Binding events and listener response functions (new article)
    event_manager.add_event_listener(EVENT_ARTICAL, listner1.read_artical)
    event_manager.add_event_listener(EVENT_ARTICAL, listner2.read_artical)
    # Start event manager
    event_manager.start()

    publicAcc = PublicAccounts(event_manager)

    # Timer(2, publicAcc.WriteNewArtical).start()

    for i in range(10):
        publicAcc.write_newartical()
        time.sleep(10)

    event_manager.stop()


if __name__ == '__main__':
    have_a_test()