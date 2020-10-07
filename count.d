#!/usr/sbin/dtrace -qs

/* countsyscalls.d -- Count system calls invoked by a process */

syscall:::entry
/pid == $1/
{
  @num[probefunc] = count();
}
