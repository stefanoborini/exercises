program ex2
    use mpi
    implicit none
    integer :: ierr, comm,rank, siz
    integer :: value(2)
    integer :: source, dest
    integer :: i
    integer :: status(MPI_STATUS_SIZE)


    call mpi_init(ierr)
    call mpi_comm_rank(MPI_COMM_WORLD, rank, ierr)
    call mpi_comm_size(MPI_COMM_WORLD, siz, ierr)

    if (rank == 0) then
        print *, "rank 0"
        do source=1,siz-1
            call mpi_recv(value, 2, MPI_INTEGER, source, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE,ierr )
            print *, "value ",value 
        enddo
    else
        print *, "rank", rank
        value(1) = rank*10
        value(2) = rank*20
        call mpi_send(value, 2, MPI_INTEGER, 0, 0, MPI_COMM_WORLD, ierr)
    endif

    call mpi_finalize(ierr)
end program

