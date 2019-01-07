
# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import os
import subprocess
import time
import sys

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class BestSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(BestSkill, self).__init__(name="BestSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("").require("Hello").require("World"))
    def handle_hello_world_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog
        self.speak_dialog("hello.world")

    @intent_handler(IntentBuilder("").require("Count").require("Dir"))
    def handle_count_intent(self, message):
        if message.data["Dir"] == "up":
            self.count += 1
        else:  # assume "down"
            self.count -= 1
        self.speak_dialog("count.is.now", data={"count": self.count})

    @intent_handler(IntentBuilder("").require("Beast"))
    def handle_best_intent(self, message):
        self.speak_dialog("da.best")

    @intent_handler(IntentBuilder("").require("Origami"))
    def handle_ORII_intent(self,message):
        self.speak_dialog("origami")
    @intent_handler(IntentBuilder("").require("Google"))
    def handle_Google_intent(self,message):
        path = "/home/herangithan/assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/grpc/textinput.py"
        p1 = "--device-id"
        p2 = "158195662888-u49u2d7mpdilq3sjq4h0dq0dto7j8uaf.apps.googleusercontent.com"
        p3 = "--device-model-id"
        p4 = "razer-project-razer_assistant_hub-wigbnw"
        #pro = subprocess.Popen(["/home/herangithan/env/bin/python3",path,p1,p2,p3,p4],stdout=subprocess.PIPE)
        pro = subprocess.Popen("/home/herangithan/env/bin/python3 " +path + " " + p1 + " " + p2 + " " + p3+  " " + p4, shell=True, stderr=subprocess.PIPE)
        while(True):
           out = pro.stderr.read(1)
           if out == '' and pro.poll() != None:
               break
           if out != '':
               sys.stdout.write(out)
               sys.stdout.flush()
        self.speak_dialog("Google Assistant has Exited")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return BestSkill()
