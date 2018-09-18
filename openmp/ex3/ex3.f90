program mandel
    integer, parameter :: max_iteration = 1000
    integer :: i,j
    integer :: iteration
    character(len=80) :: line
    real :: x0, y0, x, y, xtemp
   
!$omp parallel do private(j,x0,y0,x,y,iteration,line, xtemp)
    do i=1,40
        line = ""
        do j=1,80
            x0 = real( 4.0*real(i-20)/40.0 -1.0)
            y0 = real( 4.0*real(j-40)/80.0 +0.0)
            x=0.0
            y=0.0
            iteration = 0
            do while (x*x + y*y <= 4.0 .and. iteration < max_iteration)
                 xtemp = x*x - y*y + x0
                 y = 2.0*x*y+y0
                 x = xtemp
                 iteration = iteration + 1
            enddo
            if (iteration == max_iteration) then
                line(j:j) = "."
            else
                line(j:j) = "*"
            endif 
       enddo
        print *, line
    enddo
!$omp end parallel do
end program
