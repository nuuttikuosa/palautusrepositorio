from urllib import request
from project import Project
import toml 

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        parsed_content = toml.loads(content)
        #print(parsed_content)
        parsed_data = parsed_content["tool"]["poetry"]
        #print(parsed_data["name"])
        #print(parsed_data["description"])
        dependencies = parsed_data["dependencies"]
        #print(list(dependencies))
        dev_dependencies = parsed_data["group"]["dev"]["dependencies"]
        #print(dev_dependencies)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed_data["name"], parsed_data["description"], parsed_data["authors"],parsed_data["license"] , list(dependencies), list(parsed_data["group"]["dev"]["dependencies"]))
