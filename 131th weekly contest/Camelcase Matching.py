class Solution:

    def camelMatch(self, queries, pattern: str):
        """
        有点取巧，使用re模块
        :param queries:
        :param pattern:
        :return:
        """
        result = []
        import re
        pattern = '[a-z]*' + '[a-z]*'.join(pattern) + '[a-z]*'
        p = re.compile(pattern)
        for item in queries:
            temp = p.findall(item)
            if len(temp) > 0:
                if len(temp[0]) == len(item):
                    result.append(True)
                else:
                    result.append(False)
            else:
                result.append(False)
        return result