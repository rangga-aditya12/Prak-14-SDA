import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def tambah_edge(self, u, v, weight):
        if u in self.graph:
            self.graph[u].append((v, weight))
        else:
            self.graph[u] = [(v, weight)]

    def hapus_edge(self, u, v):
        if u in self.graph:
            self.graph[u] = [i for i in self.graph[u] if i[0] != v]

    def hapus_vertex(self, v):
        if v in self.graph:
            del self.graph[v]
        for k in self.graph:
            self.graph[k] = [i for i in self.graph[k] if i[0] != v]

    def tampilkan(self):
        print("\nRepresentasi Graph (Adjacency List):")
        for node in self.graph:
            edges = ", ".join([f"({nbr}, {weight})" for nbr, weight in self.graph[node]])
            print(f"{node} -> [{edges}]")
        print()

    def dijkstra(self, start):
        min_heap = [(0, start)]
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        visited = set()
        
        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        
        return distances

def main():
    graph = Graph()
    while True:
        print("\nMenu Operasi Graph :")
        print("1. Tambah Vertex")
        print("2. Tambah Edge")
        print("3. Hapus Edge")
        print("4. Hapus Vertex")
        print("5. Tampilkan Graph")
        print("6. Lakukan Dijkstra")
        print("7. Keluar")
        
        choice = int(input("Masukkan pilihan Anda: "))
        
        if choice == 1:
            vertex = input("Masukkan nama vertex yang ingin ditambahkan: ")
            graph.tambah_vertex(vertex)
        elif choice == 2:
            u = input("Masukkan nama vertex asal: ")
            v = input("Masukkan nama vertex tujuan: ")
            weight = int(input("Masukkan bobot edge: "))
            graph.tambah_edge(u, v, weight)
        elif choice == 3:
            u = input("Masukkan nama vertex asal: ")
            v = input("Masukkan nama vertex tujuan: ")
            graph.hapus_edge(u, v)
        elif choice == 4:
            vertex = input("Masukkan nama vertex yang ingin dihapus: ")
            graph.hapus_vertex(vertex)
        elif choice == 5:
            graph.tampilkan()
        elif choice == 6:
            start_vertex = input("Masukkan vertex awal untuk Dijkstra: ")
            distances = graph.dijkstra(start_vertex)
            print(f"\nJarak terpendek dari vertex {start_vertex}:")
            for vertex, distance in distances.items():
                print(f"{start_vertex} -> {vertex} : {distance}")
        elif choice == 7:
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
