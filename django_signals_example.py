
import time
import threading
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

# Example 1: Synchronous signal execution
class MyModel1(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel1)
def my_signal_handler_1(sender, instance, **kwargs):
    print("Signal received for:", instance.name)

def run_example_1():
    obj = MyModel1.objects.create(name="Test Example 1")
    print("Object created")  # This will run after the signal handler completes

# Example 2: Signal execution in the same thread
class MyModel2(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel2)
def my_signal_handler_2(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
    time.sleep(2)
    print("Signal handler finished")

def run_example_2():
    obj = MyModel2.objects.create(name="Test Example 2")
    print("Object created")
    print("Current thread ID:", threading.get_ident())

# Example 3: Signal running in the same transaction
class MyModel3(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel3)
def my_signal_handler_3(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
    instance.name = "Modified by Signal"
    instance.save()

def run_example_3():
    obj = MyModel3.objects.create(name="Original")
    print("Name before save:", obj.name)

    with transaction.atomic():
        obj.name = "Updated by Caller"
        obj.save()

    print("Name after save:", obj.name)


# Main function to run all examples
def main():
    print("\nRunning Example 1: Synchronous Signal Execution")
    run_example_1()

    print("\nRunning Example 2: Signal Execution in the Same Thread")
    run_example_2()

    print("\nRunning Example 3: Signal Running in the Same Transaction")
    run_example_3()

if __name__ == "__main__":
    main()
