import time
import selenium_gunb


def get_time(start_time):
    end_time = time.time()
    total_s = end_time - start_time
    total_m = int(total_s / 60)
    total_s = int(total_s - total_m * 60)
    return f"{total_m}m {total_s}s"


if __name__ == "__main__":
    main_start_time = time.time()

    start_time = time.time()
    selenium_gunb.main()
    print(f"a_4_1_1_update_published_news time: {get_time(start_time)}")




    print(f"")
    print(f"#####################################")
    print(f"Total time: {get_time(main_start_time)}")
    print(f"#####################################")
