class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def tambah_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)

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
        print("\nRepresentasi Graf (adjacency list):")
        for node in self.graph:
            print(node, "->", " -> ".join(self.graph[node]))
        print()

    def dfs_util(self, v, visited, dfs_path):
        visited.add(v)
        dfs_path.append(v)
        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, dfs_path)

    def dfs(self, start):
        visited = set()
        dfs_path = []  # Inisialisasi jalur penelusuran DFS
        self.dfs_util(start, visited, dfs_path)
        return dfs_path  # Mengembalikan jalur penelusuran DFS

def main():
    graph = Graph()
    while True:
        print("\nMenu Operasi Graph:")
        print("1. Tambah Vertex")
        print("2. Tambah Edge")
        print("3. Hapus Edge")
        print("4. Hapus Vertex")
        print("5. Tampilkan Graf")
        print("6. Penelusuran DFS")
        print("7. Keluar")
        choice = int(input("Pilih operasi yang diinginkan: "))
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
            start_vertex = input("Masukkan nama vertex awal untuk DFS: ")
            dfs_path = graph.dfs(start_vertex)
            print(f"\nPenelusuran DFS dimulai dari vertex {start_vertex}: ", end='')
            print(" -> ".join(dfs_path))
        elif choice == 7:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
