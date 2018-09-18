program ex2
    implicit none
    integer, parameter :: n=3000000
    integer :: i
    real :: z(n), a, x(n), y

    a=1.0d0
    y=2.0d0

    do i=1,n
        x(i) = 0.0d0
    enddo

    call saxpy(z,a,x,y,n)

end program


subroutine saxpy(z,a,x,y,n)
   implicit none
   integer, intent(in) :: n
   real, intent(out) :: z(n)
   real, intent(in) :: a, x(n), y
   integer :: i
!$omp parallel do private(i)
   do i=1,n
       z(i) = a*x(i) + y
   enddo
!$omp end parallel do
end subroutine
