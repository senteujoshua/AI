class Graphs:
    def __init__(self, edges):
        self.edges =edges
        self.flight_dict = {}
        for start,end in self.edges:
            if start in self.flight_dict:
                self.flight_dict[start].append(end)
            else:
                self.flight_dict[start] = [end]


    def get_paths(self,start,end,path=None):
        if path is None:
            path = []
            path = path +[start]

        if start == end:
            return [path]
        if start not in self.flight_dict:
            return []
        for node in self.flight_dict[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    path.append(p)

        return path

    def __str__(self):
        return f'Flight Routes: \n {self.flight_dict}'
    



  
if __name__ =='__main__':

    flight_routes = [
        ("Nairobi", "Lagos"),
        ("Nairobi", "Accra"),
        ("Nairobi", "Johannesburg"),
        ("Lagos", "Dubai"),
        ("Accra", "London"),
        ("Johannesburg", "Cairo"),
        ("Dubai", "Mumbai"),
        ("London", "New York"),
        ("Cairo", "Paris"),
        ("Mumbai", "Singapore"),
        ("Paris", "Berlin"),
        ("New York", "Toronto"),
        ("Toronto", "Vancouver"),
        ("Berlin", "Rome"),
        ("Singapore", "Sydney"),
        ("Sydney", "Auckland"),
        ("Rome", "Athens"),
        ("Athens", "Istanbul"),
        ("Istanbul", "Moscow"),
        ("Moscow", "Beijing"),
        ("Beijing", "Tokyo"),
        ("Tokyo", "Seoul"),
    ]

route_graph = Graphs(flight_routes)
print(route_graph)
start = "Nairobi"
end = "Tokyo"
print(f'Paths between {start} and {end}:',route_graph.get_paths(start,end))