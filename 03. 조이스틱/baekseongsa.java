
class Solution {
	public int solution(String name) {
		int answer = 0;
		int exp = name.length() - 1;
		char[] arr = name.toCharArray();

		for (int i = 0; i < arr.length; i++) {
			char c = arr[i];
			answer += ('Z' - c + 1) > c - 'A' ? c - 'A' : ('Z' - c + 1);
			if (c == 'A') {
				int nextIdx = i + 1;
				int countA = 0;
				while (nextIdx < arr.length && arr[nextIdx] == 'A') {
					countA++;
					nextIdx++;
				}
				int tmp = (i - 1) * 2 + (arr.length - 1 - i - countA);
				if (exp > tmp)
					exp = tmp;
				i = nextIdx - 1;
			}
		}

		return answer + exp;
	}
}