from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.matcher = matcher

    def playsIn(self,team):
        return QueryBuilder(And(PlaysIn(team),self.matcher))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value,attr),self.matcher))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value,attr),self.matcher))
    
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1,m2))

    def build(self):
        return self.matcher