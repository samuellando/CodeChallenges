class Foo {

  private volatile boolean printedFirst;
  private volatile boolean printedSecound;

  public Foo() {
    printedFirst = false;
    printedSecound = false;
  }

  public synchronized void first(Runnable printFirst) throws InterruptedException {
    // printFirst.run() outputs "first". Do not change or remove this line.
    printFirst.run();
    printedFirst = true;
    notifyAll();
  }

  public synchronized void second(Runnable printSecond) throws InterruptedException {
    while (!printedFirst)
      wait();
    // printSecond.run() outputs "second". Do not change or remove this line.
    printSecond.run();
    printedSecound = true;
    notifyAll();
  }

  public synchronized void third(Runnable printThird) throws InterruptedException {
    while (!printedSecound)
      wait();
    // printThird.run() outputs "third". Do not change or remove this line.
    printThird.run();
  }
}
