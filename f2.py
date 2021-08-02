def run_import_module():
  print(f"f2 is a importable module")
  print(f"f2:{__name__}")

def main():
  print(f"f2 is the main program")
  print(f"f2:{__name__}")

if __name__ == "__main__":
  main()
