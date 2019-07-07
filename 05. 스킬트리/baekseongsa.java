class Solution {
	public int solution(String skill, String[] skill_trees) {
		int answer = 0;

		for (int i = 0; i < skill_trees.length; i++) {
			String skill_tree = skill_trees[i];
			boolean result = true;
			int index = 0;
			char prevSkill = skill.charAt(0);

			for (int j = 0; j < skill_tree.length(); j++) {
				char c = skill_tree.charAt(j);

				if (skill.indexOf(c) == -1)
					continue;

				if (prevSkill != c) {
					result = false;
					break;
				}

				if (index < skill.length() - 1) {
					prevSkill = skill.charAt(++index);
				} else {
					result = true;
					break;
				}
			}

			if (result) answer++;
		}

		return answer;
	}
}