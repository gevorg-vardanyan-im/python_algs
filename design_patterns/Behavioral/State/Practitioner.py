from design_patterns.Behavioral.State.Activity import Activity
from design_patterns.Behavioral.State.Bear import Bear
from design_patterns.Behavioral.State.Boar import Boar
from design_patterns.Behavioral.State.Buffalo import Buffalo
from design_patterns.Behavioral.State.Crow import Crow
from design_patterns.Behavioral.State.Eagle import Eagle
from design_patterns.Behavioral.State.Finist import Finist
from design_patterns.Behavioral.State.Horse import Horse
from design_patterns.Behavioral.State.Lynx import Lynx
from design_patterns.Behavioral.State.Moose import Moose
from design_patterns.Behavioral.State.Pike import Pike
from design_patterns.Behavioral.State.Snake import Snake
from design_patterns.Behavioral.State.Stork import Stork
from design_patterns.Behavioral.State.Swan import Swan
from design_patterns.Behavioral.State.Virgo import Virgo
from design_patterns.Behavioral.State.Wolf import Wolf


class Practitioner:
    """docstring for Practitioner"""

    activity: Activity

    def set_activity(self, activity: Activity):
        self.activity = activity

    def change_activity(self):
        if isinstance(self.activity, Virgo):
            self.set_activity(Boar())
        elif isinstance(self.activity, Boar):
            self.set_activity(Pike())
        elif isinstance(self.activity, Pike):
            self.set_activity(Swan())
        elif isinstance(self.activity, Swan):
            self.set_activity(Snake())
        elif isinstance(self.activity, Snake):
            self.set_activity(Crow())
        elif isinstance(self.activity, Crow):
            self.set_activity(Bear())
        elif isinstance(self.activity, Bear):
            self.set_activity(Stork())
        elif isinstance(self.activity, Stork):
            self.set_activity(Wolf())
        elif isinstance(self.activity, Wolf):
            self.set_activity(Buffalo())
        elif isinstance(self.activity, Buffalo):
            self.set_activity(Moose())
        elif isinstance(self.activity, Moose):
            self.set_activity(Finist())
        elif isinstance(self.activity, Finist):
            self.set_activity(Horse())
        elif isinstance(self.activity, Horse):
            self.set_activity(Eagle())
        elif isinstance(self.activity, Eagle):
            self.set_activity(Lynx())
        elif isinstance(self.activity, Lynx):
            self.set_activity(Virgo())

    def move(self):
        self.activity.evolve()
