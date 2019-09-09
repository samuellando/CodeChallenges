ss Solution:
def numUniqueEmails(self, emails: List[str]) -> int:
  table = {}
  count = 0
  for email in emails:
    local = email.split("@")[0]
    public = email.split("@")[1]
    local = local.replace(".","")
    local = re.sub(r'\+.*$',"",local)
    if not local+"@"+public in table:
      table[local+"@"+public] = True
      count += 1
  return count
