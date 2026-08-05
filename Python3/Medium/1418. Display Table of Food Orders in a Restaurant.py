class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        Table = {}

        for i in range(len(orders)):
            Table_no = orders[i][1]
            Food = orders[i][2]

            if Table_no not in Table:
                Table[Table_no] = {}

            if Food not in Table[Table_no]:
                Table[Table_no][Food] = 0

            Table[Table_no][Food] += 1


        foods = sorted({food for table in Table.values() for food in table})
        
        result = [["Table"] + foods]


        for table in sorted(Table,key=int):
            row = [table]
            for food in foods:
                row.append(str(Table[table].get(food,0)))
            result.append(row)

        return result