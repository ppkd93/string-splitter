class TagManipulator():
    def parse_string(self, tags):
        if tags == "," or tags == "":
            result = []
            return result
        
        result = tags.split(",")

        if len(tags) < 1 :
            return result

        return result