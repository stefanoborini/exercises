program ex1
    implicit none
    integer :: omp_get_thread_num
!$omp parallel
    print "(I3)", omp_get_thread_num()
!$omp end parallel
end program 
