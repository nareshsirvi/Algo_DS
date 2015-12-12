
def top_sort(adj_list):
    reverse_po = []
    visited = [False] * len(adj_list)

    for i in range(len(adj_list)):
        if not visited[i]:
            dfs = [i]
            visited[i] = True
            while dfs:
                top = dfs[-1]
                used = False
                for adj in adj_list[top]:
                    if not visited[adj]:
                        dfs.append(adj)
                        visited[adj] = True
                        used = True
                
                if not used:
                    reverse_po.append(top)
                    dfs.pop()

    reverse_po.reverse()
    return reverse_po

if __name__ == '__main__':
    # adj_list = [[1, 2, 3], [4], [4], [4], []]
    adj_list = [[], [0], [0], [1, 2], [1, 3]]
    print top_sort(adj_list)
