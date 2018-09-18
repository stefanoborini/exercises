program ex1
    use mpi
    implicit none
    integer :: err, comm,rank, siz
    integer :: info = -1
    call mpi_init(err)
    comm = MPI_COMM_WORLD 
    call mpi_comm_rank(comm, rank, err)
    call mpi_comm_size(comm, siz, err)

    if (rank == 0) then
        info = 42
    endif

    print *, "rank = ", rank, "info = ", info

    call MPI_Barrier(MPI_COMM_WORLD, err)

    call MPI_Bcast(info, count=1, datatype=MPI_INTEGER, root=0, comm=MPI_COMM_WORLD, ierror=err)
   
    print *, "rank = ", rank, "info = ", info

    call mpi_finalize(err)
end program
