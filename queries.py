import rdflib


class Queries:
  def __init__(self):
    self.g = rdflib.Graph()
    self.g.load("three_kingdoms.rdf", format="turtle")

  def birthplace(self, subj, place):
    qres = self.g.query(
      """SELECT DISTINCT ?name ?ancient_birthplace ?modern_birthplace
         WHERE {
            ?person foaf:ancient_birthplace ?ancient_birthplace .
            ?person foaf:modern_birthplace ?modern_birthplace .
            ?person foaf:name ?name .
         }""")

    for row in qres:
      name = row[0]
      ancient_birthplace = row[1]
      modern_birthplace = row[2]

      ########################
      # Where was person A born
      ########################
      if subj:
        if str(name) == subj:
          print("{}'s ancient birthplace was {}, which is modern-day {}.".format(name, ancient_birthplace, modern_birthplace))

      ########################
      # Who was born in place A
      ########################
      elif place:
        if str(ancient_birthplace) == place or str(modern_birthplace) == place:
          print("{} was born in {}, modern-day {}.".format(name, ancient_birthplace, modern_birthplace))
      else:
        raise NotImplementedError

  def loyalty(self, subj, pred):
    qres = self.g.query(
       """SELECT DISTINCT ?charname ?leadername
          WHERE {
             ?person foaf:loyal_to ?leadername .
             ?person foaf:name ?charname .
          }""")

    for row in qres:
      subject = row[0]
      predicate = row[1]

      ########################
      # Who was loyal to person A?
      ########################
      if not subj:
        if str(predicate) == pred:
          print("{} has loyalty from {}.".format(pred, subject))

      ########################
      # Who person A loyal to?
      ########################
      else:
        if str(subject) == subj:
          print("{} is loyal to {}.".format(subject, predicate))

  def lifespan(self, subj):
    qres = self.g.query(
      """SELECT DISTINCT ?charname ?lifespan
      WHERE{
          ?person foaf:birth ?lifespan .
          ?person foaf:name ?charname .
      }""")

    for row in qres:
      name = row[0]
      lifespan = row[1]
      if str(name) == subj:
        print("{} lived was alive the following years: {}.".format(name, lifespan))

  def gender(self, subj, gender):
    qres = self.g.query(
      """SELECT DISTINCT ?charname ?gender
      WHERE{
          ?person foaf:gender ?gender .
          ?person foaf:name ?charname .
      }""")

    for row in qres:
      name = row[0]
      gen = row[1]

      ########################
      # What gender was Person A?
      ########################
      if subj:
        if str(name) == subj:
          print("{} was {}.".format(name, gen))

      ########################
      # Which characters were male?
      ########################
      elif gender:
        if str(gen) == gender:
          print("{} was {}.".format(name, gen))

      else:
        raise NotImplementedError


if __name__ == '__main__':
    templates = Queries()
    # templates.loyalty("丁斐", None)
    # templates.birthplace(None, "豫州沛国")
    # templates.lifespan("丁仪")
    templates.gender("丁仪", None)