path_performance = dict()

def main():

    with open('./logs.txt', 'r') as f:
        for line in f.readlines():
            (path, time_) = line.split(' ')

            if path not in path_performance:
                path_performance[path] = {
                    'total_requests': 0,
                    'performance':{
                        'less_than_100ms':0,
                        'between_100_and_300ms': 0,
                        'between_300_and_1s' : 0,
                        'greater_than_1s': 0
                    }
                }

            time_ = int(time_)
            path_performance[path]['total_requests'] += 1
            if time_ < 100:
                path_performance[path]['performance']['less_than_100ms'] += 1
            elif time_ >=100 and time_<300:
                path_performance[path]['performance']['between_100_and_300ms'] += 1
            elif time_ >=300 and time_<1000:
                path_performance[path]['performance']['between_300_and_1s'] += 1
            else:
                path_performance[path]['performance']['greater_than_1s'] += 1

if __name__ == '__main__':
    main()
    for item in path_performance:
        print(item)