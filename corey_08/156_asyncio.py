# asyncio is python lib using to write concurrent code using async await syntax

# what is concurrency

# synchronous code exec (normal code we write)
# one thing happens then another
# its like a mini restaurant they stop make food for u then after sevring u go for next one

# whereas asynchronous code
# its like ask u r while making u r order take others orders too while prep u r food at background
# asynchronous dont automatically means faster it juts means we can do other useful owrk 
# instead of sitting idle by while waiting for things like network queries, db etc
# so asyncio excels at IOBound tasks in whihc prog wiats for external

# asyncio is singe threaded and runs on single process
# it uses co-operative multitasking where tasks voluntarily give up control
# for cpu bound tasks that need haevy computation want to use process instead
# we will see diff be IOBound and CPUBound 

# eventloop is basically the engine that runs and manages async funcs
# think of it like scheduler it keep track of all our tasks 
# when a task is suspended since its waiting for help 
# control returns to event loop
# chihc is returned another task to either start or resume

# so we have to running our eventloop for any of our async code
# async keyowrd before fun def and asyncio.run(async_func) to make event loop
# that is responsible for getting the evnt loop running task until they r marked as complete
# and then closing event loop whenever its doen

# we want to use concurrency isnide our event loop
# to use this concurrency we r gonna use await keyword a lot
# we r using await keyword so awaitables are objects that implements
# a special method __await__() under the hood
# we r gonna use await keyword in all asycn code

# an obj has to be awaitable for us to use that keyword on
# now why cant we await a sync function
# well sync lib dont have mechanisms to work with event loop
# they dont know how to control yield control over and resume later
# so sync code like time.sleep()or any sync func 
# these dont have undelrying special await function
# that they need in order to pause their execution and st back later
# also we have to inside async func to use await

# so waht does await do
# u r basically telling the event loop
# to pause the exec of current one func and yield control back to event loop
# which can then run another task ans its stays suspendable 
# until thsi awaitables completed

# in python asyncio there r 3 main awaitable objects
# 1. coroutines (which r created when you call an async func)
# 2. tasks (r wrappers around coroutines that r scheduled on event loop)
# 3. futures (r low level objects representing eventual resulst)
# futures r lot like promises in js
# they r promise of a result that thye will arrive later
# but unlike js in python we almost never work with futures directly
# we write coroutines n wehn we schedule them as tasks 
# asyncio uses futures under the hood to track those results 
# but we wont be seeing much internal details   
# we will only use futures directly when u r writing low level async io code
# like if u r building async io compatible framweok

# so a future job is to hold a certain state and result
# the state can be pernding menaing the future dont have any resukt or exception yet
# it can be cancelled if it was cancelledusing future.cancelled
# or it can be finished by aresult being set by future.set_result()
# or it can be an exception by future.set_exception()

# co routines are func with asycn def keyword 
# so main and async_function are coroutine functions
# async fucn is also same as sync unc but we used asyncio.slepp() over time.sleep()
# and also we r awaiting it as well
# so coroutines n basically objects whose exceution we can pause
# and there r 2 main terms 
# coroutine function -> what we define async def keyword 
# coroutine object -> which will be awaitable that gets returned wehn we call that function
# so async_function is a coroutine function whereas obj returend n stored in coroutine_obj is coroutine object

# so coroutines r bit like generators in sesnse they can suspend exec n resume later
# but they r designed to work for an event loop 
# they have extra feature that asyncio needs to schedule them await io n coord mult tasks

# when this is called
# sync_function("Test")
# it runs whole function and thats ended
# whereas async_function("Test") returned coroutine object
# and we have exec the coroutine obj to run this n het result
# we have to await it wehn i await it await coroutine_obj
# then only it started exec it and then we got the result
# when we directly await coroutine obj like this 
# it both scheduled on the event loop and run to completion at the same time

# now tasks are wrapped coroutines that can be exec independently
# tasks r actaully how we run coroutines concurrently
# when we wrap a coroutine in task using asyncio.create_task()
# then its handed over the event loop and scheduled to run whenver its gets a chance
# task will keep track of corouitne ie finished successfully, raise error or got cancelled just lie a future
# in fact tasks r futures under the hood but with extra logic 
# to actually run the coroutine and do the work we wanted to 
# thats why we work with tasks instead of futures in most of code

# but unlike coroutine ojects tasks can be scheduled on event loop 
# and can just sit there without being run until the loops get control 
# thsi is the key to async io
# you can queue multiple atsks at once
# and then event loop will be able to run them whenever its ready
# letting them take turns while waiting on IO


import asyncio
import time

def sync_function(test_param: str) -> str:
    print("This is a synchronous function")
    time.sleep(0.1)
    return f"Sync Result: {test_param}"

async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function")
    await asyncio.sleep(0.1)
    return f"Async Result: {test_param}"

async def main():
    sync_result = sync_function("Test")
    print(sync_result)
    # This is a synchronous function
    # Sync Result: Test

    # # low level code that we dont use mostly
    # loop = asyncio.get_running_loop()
    # # future is like a promise object
    # future = loop.create_future()
    # print(f"Empty future: {future}")

    # future.set_result("Future Result: Test")
    # future_result = await future
    # print(future_result)

    # coroutine_obj = async_function("Test")
    # print(coroutine_obj)
    # # <coroutine object async_function at 0x000001C000EE0D40>

    # coroutine_result = await coroutine_obj
    # # This is an asynchronous coroutine function
    # print(coroutine_result)
    # # Async Result: Test

    task = asyncio.create_task(async_function("Test"))
    print(task)
    # <Task pending name='Task-2' coro=<async_function() running at O:\tut\corey_08\156_asyncio.py:120>>
    task_result = await(task)
    # This is an asynchronous coroutine function
    print(task_result)
    # Async Result: Test

