class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleague_list = []

    def add_actor_colleague(self,other):
        if not isinstance(other, Actor):
            pass
        self.__colleague_list.append(other)

    def check_if_this_actor_worked_with(self,colleague):
        if colleague in self.__colleague_list:
            return True
        return False

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def colleague_list(self):
        return self.__colleague_list

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return other.__actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        if self.actor_full_name > other.actor_full_name:
            return False
        else:
            return True

    def __hash__(self):
        return hash(self.__actor_full_name)

