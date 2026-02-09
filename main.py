from dynamic_arr_implementation import DynamicArray

if __name__ == "__main__":
    print("=== Testing DynamicArray ===\n")
    
    arr = DynamicArray()
    print(f"Initial: {arr}")
    print(f"Empty? {arr.is_empty()}\n")  # ✅ Use is_empty(), not __is_empty__()
    
    # Test append and capacity doubling
    print("--- Appending elements ---")
    for i in range(5):
        arr.append(i * 10)
        print(f"After append({i * 10}): {arr}")
    print()
    
    # Test get
    print("--- Testing get() ---")
    print(f"arr.get(0) = {arr.get(0)}")
    print(f"arr.get(4) = {arr.get(4)}")
    try:
        arr.get(10)
    except IndexError as e:
        print(f"✅ Correctly raised: {e}")
    print()
    
    # Test set
    print("--- Testing set() ---")
    arr.set(2, 999)
    print(f"After arr.set(2, 999): {arr}")
    try:
        arr.set(10, 100)
    except IndexError as e:
        print(f"✅ Correctly raised: {e}")
    print()
    
    # Test with None values
    print("--- Testing with None ---")
    arr.append(None)
    print(f"After append(None): {arr}")
    print(f"arr.get(5) = {arr.get(5)}")