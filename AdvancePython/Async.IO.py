import asyncio


# coroutine function 
async def main( ):
    print('start of couratine')

#  **********  async main()*******************
# when we define the main funcrion with the async it will return a courotine object     

#  main() it will generate the error because main as define as a croutine object 

# run the main coroutine
asyncio.run(main())



# Define a coroutine that simulates a time_consuming task 
async def fetch_data(delay):
    print("Fetching data......")
    await asyncio.sleep(delay)    # simulate an I/O operation with a sleep 
    print("Data fetched")
    return {"data" : "Some Data"}



# define another coroutine that calls the first couritine
async def coroutine_caller():
    print("Start of the caller")

    task =  fetch_data(2)
    # task = await fetch_data(2)
    #Await the fetch_data coroutine , pausing the execution of caller untill the fetch_data completes

    print("End of caller before wait ")
    
    result = await task
    
    print(f"Recieved Result: {result}")
    
    print("End of caller after wait ")


asyncio.run((coroutine_caller()))





async def fetch_data_mulitple(delay , id):
    print("Fetching data.....id" , id)
    await asyncio.sleep(delay)    # simulate an I/O operation with a sleep 
    print("Data fetched")
    return {"data" : "Some Data" , "id" : id}


async def coroutine_caller_mulitiple():
    print("Start of the caller")

    task1 =  fetch_data_mulitple(2 , 1)    
    result1 = await task1
    print(f"Recieved Result: {result1}")

    task2 =  fetch_data_mulitple(2 , 2)    
    result2 = await task2
    print(f"Recieved Result: {result2}")
    
    print("End of caller after wait ")

asyncio.run((coroutine_caller_mulitiple()))


# as we see from the above implementation i get that for the 2nd task have to wait for the 1st to complete 



 


async def func1():
	print("Function 1 started..")
	await asyncio.sleep(2)
	print("Function 1 Ended")


async def func2():
	print("Function 2 started..")
	await asyncio.sleep(3)
	print("Function 2 Ended")


async def func3():
	print("Function 3 started..")
	await asyncio.sleep(1)
	print("Function 3 Ended")


async def gather():
	L = await asyncio.gather(
		func1(),
		func2(),
		func3(),
	)
	print("Main Ended..")


asyncio.run(gather())
