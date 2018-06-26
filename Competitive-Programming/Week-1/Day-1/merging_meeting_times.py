import unittest
def merge_ranges(meetings):

    meetings.sort(key=lambda interval: interval[0])
    merged = [meetings[0]]
    for current in meetings:
    	previous = merged[-1]
    	if current[0] <= previous[1]:
    		previous[1] = max(previous[1], current[1])
    	else:
        	merged.append(current)
    return merged

# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([[1, 3], [2, 4]])
        expected = [[1, 4]]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([[5, 6], [6, 8]])
        expected = [[5, 8]]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([[1, 8], [2, 5]])
        expected = [[1, 8]]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([[1, 3], [4, 8]])
        expected = [[1, 3], [4, 8]]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([[1, 4], [2, 5], [5, 8]])
        expected = [[1, 8]]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([[0, 1], [3, 5], [4, 8], [10, 12], [9, 10]])
        expected = [[0, 1], [3, 8], [9, 12]]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)