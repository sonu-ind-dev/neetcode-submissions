class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueMails = []

        for mail in emails:
            uniqueMail = ''
            isDomainChar = False
            hadPlusChar = False

            for mailChar in mail:
                if mailChar == '@':
                    isDomainChar = True
                elif mailChar == '+':
                    hadPlusChar = True

                if isDomainChar or (mailChar != '.' and hadPlusChar == False):
                    uniqueMail += mailChar
            
            if uniqueMail not in uniqueMails:
                uniqueMails.append(uniqueMail)

        return len(uniqueMails)