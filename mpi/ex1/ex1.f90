program ex1
    use mpi
    implicit none
    integer :: ierr, comm,rank, siz
    call mpi_init(ierr)
    comm = MPI_COMM_WORLD 
    call mpi_comm_rank(comm, rank, ierr)
    call mpi_comm_size(comm, siz, ierr)
    print *, "hello",rank, siz
    call mpi_finalize(ierr)
end program
