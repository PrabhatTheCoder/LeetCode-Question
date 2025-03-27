class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        attempts = 0

        while students and attempts < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                attempts = 0
            else:
                students.append(students.pop(0))
                attempts += 1

        return len(students)

        