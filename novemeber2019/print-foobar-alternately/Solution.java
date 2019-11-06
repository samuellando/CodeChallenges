class FooBar {
  private int n;
  private volatile boolean printfoo;

  public FooBar(int n) {
    this.n = n;
    printfoo = true;
  }

  public synchronized void foo(Runnable printFoo) throws InterruptedException {
    for (int i = 0; i < n; i++) {
      while (!printfoo) 
        wait();
      // printFoo.run() outputs "foo". Do not change or remove this line.
      printFoo.run();
      printfoo = false;
      notifyAll();
    }
  }

  public synchronized void bar(Runnable printBar) throws InterruptedException {

    for (int i = 0; i < n; i++) {
      while (printfoo) 
        wait();
      // printBar.run() outputs "bar". Do not change or remove this line.
      printBar.run();
      printfoo = true;
      notifyAll();
    }
  }
}
