#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int longestBalanced(string s) {
    int oneChar = longestSingleChar(s);

    int twoChar =
        max({longestTwoChars(s, 'a', 'b'), longestTwoChars(s, 'a', 'c'),
             longestTwoChars(s, 'b', 'c')});

    int threeChar = longestThreeChars(s);

    return max({oneChar, twoChar, threeChar});
  }

private:
  // -----------------------------
  // Case 1: only one character
  // -----------------------------
  int longestSingleChar(string s) {
    int n = s.size();
    int ans = 0;

    int i = 0;
    while (i < n) {
      int j = i;

      while (j < n && s[j] == s[i])
        j++;

      ans = max(ans, j - i);
      i = j;
    }
    return ans;
  }

  // -------------------------------------------
  // Case 2: two characters with equal counts
  // -------------------------------------------
  int longestTwoChars(string s, char a, char b) {
    int n = s.size();
    int ans = 0;
    int i = 0;

    while (i < n) {

      // skip unrelated characters
      while (i < n && s[i] != a && s[i] != b)
        i++;

      unordered_map<int, int> firstIndex;
      firstIndex[0] = i - 1;

      int diff = 0;

      while (i < n && (s[i] == a || s[i] == b)) {

        if (s[i] == a)
          diff++;
        else
          diff--;

        if (firstIndex.count(diff))
          ans = max(ans, i - firstIndex[diff]);
        else
          firstIndex[diff] = i;

        i++;
      }
    }

    return ans;
  }

  // ----------------------------------------
  // Case 3: all three characters equal
  // ----------------------------------------
  int longestThreeChars(string s) {
    unordered_map<long long, int> firstIndex;

    // helper to combine two ints into one key
    auto makeKey = [](int x, int y) {
      return ((long long)x << 32) ^ (unsigned int)y;
    };

    int countA = 0, countB = 0, countC = 0;
    int ans = 0;

    firstIndex[makeKey(0, 0)] = -1;

    for (int i = 0; i < s.size(); i++) {

      if (s[i] == 'a')
        countA++;
      else if (s[i] == 'b')
        countB++;
      else
        countC++;

      int d1 = countA - countB;
      int d2 = countB - countC;

      long long key = makeKey(d1, d2);

      if (firstIndex.count(key))
        ans = max(ans, i - firstIndex[key]);
      else
        firstIndex[key] = i;
    }

    return ans;
  }
};
