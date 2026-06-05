"""
468. Validate IP Address
https://leetcode.com/problems/validate-ip-address/
Difficulty: Medium  Topic: String

Return "IPv4", "IPv6", or "Neither".

IPv4: four dot-separated decimal octets, each 0-255 with no leading zeros.
IPv6: eight colon-separated groups of 1-4 hex digits.
"""

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(ip: str) -> bool:
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or int(part) > 255 or str(int(part)) != part:
                    return False
            return True

        def is_ipv6(ip: str) -> bool:
            allowed = set("0123456789abcdefABCDEF")
            parts = ip.split(":")
            if len(parts) != 8:
                return False
            for part in parts:
                if not (1 <= len(part) <= 4) or any(c not in allowed for c in part):
                    return False
            return True

        if "." in queryIP:
            return "IPv4" if is_ipv4(queryIP) else "Neither"
        if ":" in queryIP:
            return "IPv6" if is_ipv6(queryIP) else "Neither"
        return "Neither"
