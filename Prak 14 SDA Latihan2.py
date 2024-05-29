from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def tambah_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def hapus_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

    def hapus_vertex(self, v):
        if v in self.graph:
            del self.graph[v]
        for k in self.graph:
            if v in self.graph[k]:
                self.graph[k].remove(v)

    def tampilkan(self):
        print("\nRepresentasi Graph (Adjacency List):")
        for node in self.graph:
            print(node, "->", self.graph[node])
        print()

    def bfs(self, start):
        visited = set()
        bfs_path = []
        queue = deque([start])
        visited.add(start)
        
        while queue:
            v = queue.popleft()
            bfs_path.append(v)
            
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return bfs_path

def main():
    graph = Graph()
    while True:
        print("\n=== Operasi Graph (BFS) ===")
        print("1. Tambah Vertex")
        print("2. Tambah Edge")
        print("3. Hapus Edge")
        print("4. Hapus Vertex")
        print("5. Tampilkan Graph")
        print("6. Lakukan BFS")
        print("7. Keluar")
        print("===========================")
        choice = int(input("Masukkan pilihan Anda: "))
        
        if choice == 1:
            vertex = input("Masukkan nama vertex yang ingin ditambahkan: ")
            graph.tambah_vertex(vertex)
        elif choice == 2:
            u = input("Masukkan nama vertex asal: ")
            v = input("Masukkan nama vertex tujuan: ")
            graph.tambah_edge(u, v)
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
            start_vertex = input("Masukkan vertex awal untuk BFS: ")
            bfs_path = graph.bfs(start_vertex)
            print(f"\nPenelusuran BFS dimulai dari vertex {start_vertex}: ", end='')
            print(" -> ".join(bfs_path))
        elif choice == 7:
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
