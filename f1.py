from f2 import run_import_module

def main():
  print(f"f1 is the main program")
  print(f"f1:{__name__}")

  run_import_module()

if __name__ == "__main__":
  main()
else:
  print("f1 is an import")