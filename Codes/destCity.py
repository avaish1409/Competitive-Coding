class Solution:
    def destCity(self, paths: [[str]]):
        res = []
        starts = []
        for i in range(len(paths)):
            starts.append(paths[i][0])
            if paths[i][1] not in starts:
                res.append(paths[i][1])
            # for i in res:
            #     if
            # print(starts)
        for i in res:
            if i not in starts:
                return i


s = Solution()
print(s.destCity([["jMgaf WaWA","iinynVdmBz"],[" QCrEFBcAw","wRPRHznLWS"],["iinynVdmBz","OoLjlLFzjz"],["OoLjlLFzjz"," QCrEFBcAw"],["IhxjNbDeXk","jMgaf WaWA"],["jmuAYy vgz","IhxjNbDeXk"]]))
