class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const replaced = s.replaceAll(/[^a-zA-Z0-9]/g, '').toLowerCase();
        return replaced === replaced.split("").reverse().join("")
    }
}
