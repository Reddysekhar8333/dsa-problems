import heapq
def dijkstra(start,end,graph):
    dist={nod:float("inf") for nod in graph}
    visit={nod:False for nod in graph}
    prev={nod:None for nod in graph}
    dist[start]=0
    pri_queue=[(0,start)]
    while pri_queue:
        cur_dis,cur_n=heapq.heappop(pri_queue)
        visit[cur_n]=True
        '''if cur_n==end:
            break'''
        for nei,wei in graph[cur_n]:
            new_dis=cur_dis+wei
            if visit[nei]==True:
                continue
            if new_dis<dist[nei]:
                dist[nei]=new_dis
                prev[nei]=cur_n
                heapq.heappush(pri_queue,(new_dis,nei))
    #now traversing the path
    path = []
    curr = end
    while curr is not None:
        path.insert(0, curr)
        curr = prev[curr]
    return f"path={path}\ndistance={dist[end]}"
graph={"a":[('b',1),('c',4)],
       "b":[('a',1),('c',2),('d',5)],
       "c":[('a',4),('b',2),('d',1)],
       "d":[('b',5),('c',1)]
      }
print(dijkstra('a','d',graph))

            
            
        
