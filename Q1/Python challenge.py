def calculate_allocation(num_students):
    # Calculate the number of classes needed
    num_classes = num_students // 30 + 1 if num_students % 30 != 0 else num_students // 30

    # Calculate the number of students per class
    students_per_class = num_students // num_classes

    # Calculate the remaining students to distribute
    remaining_students = num_students % num_classes

    # Create the allocation dictionary
    allocation = {}
    for i in range(1, num_classes + 1):
        if i <= remaining_students:
            allocation[f"Class {i}"] = students_per_class + 1
        else:
            allocation[f"Class {i}"] = students_per_class

    # Print the proposed allocation
    print("Proposed Allocation:", num_classes, "classes")
    print(allocation)


# Test cases
calculate_allocation(31)
calculate_allocation(59)
calculate_allocation(87)