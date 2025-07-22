class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        visited = set()
        while queue:

            qLen = len(queue)

            for _ in range(qLen):

                node, cnt = queue.popleft()

                if node == target:
                    return cnt

                for i in range(4):

                    up = str((int(node[i]) + 1) % 10)

                    down = str((int(node[i]) - 1) % 10)

                    upNode = node[:i] + up + node[i+1:]

                    downNode = node[:i] + down + node[i+1:]

                    if upNode not in visited and upNode not in deadends:
                        queue.append((upNode, cnt + 1))
                        visited.add(upNode)
                    if downNode not in visited and downNode not in deadends:
                        queue.append((downNode, cnt + 1))
                        visited.add(downNode)
                    

        return -1




            
            
            
            
            
