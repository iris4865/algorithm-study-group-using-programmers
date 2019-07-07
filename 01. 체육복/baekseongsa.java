
class Solution {
	public int solution(int n, int[] lost, int[] reserve) {
		int answer = n;

		int[] arr = new int[n + 1];
		for (int i = 0; i < lost.length; i++) {
			arr[lost[i]] = -1;
			answer--;
		}

		for (int i = 0; i < reserve.length; i++) {
			if (arr[reserve[i]] == -1) {
				arr[reserve[i]] = reserve[i] = 0;
				answer++;
			}
		}

		for (int i = 0; i < reserve.length; i++) {
			if (reserve[i] == 0)
				continue;

			int index = reserve[i];
			if (arr[index - 1] == -1) {
				reserve[i] = arr[index - 1] = 0;
				answer++;
			} else if (index + 1 < n && arr[index + 1] == -1) {
				reserve[i] = arr[index + 1] = 0;
				answer++;
			}
		}

		return answer;
	}
}