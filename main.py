
def count_batteries_by_health(present_capacities):
  counts= {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for cap in present_capacities:
    soh =(cap/120)*100    #calculating soh as percentage
    if soh>80:
      counts["healthy"]+=1
    elif 63<=soh<=80:
      counts["exchange"]+=1
    else:
      counts["failed"]+=1
  return counts
      
    


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
