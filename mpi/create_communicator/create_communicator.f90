program create_communicator
    use mpi
    implicit none
    integer :: err, comm,rank, siz, new_rank
    integer :: value(2)
    integer :: source, dest
    integer :: i
    integer :: group, new_group, new_comm
    integer :: group_size
    integer :: rank_list(1024)
    integer :: info = -1

    call MPI_Init(err)
    call MPI_Comm_rank(MPI_COMM_WORLD, rank, err)
    call MPI_Comm_size(MPI_COMM_WORLD, siz, err)

    do i=1,(siz/2)
        rank_list(i) = (i-1)*2
    enddo
    call MPI_Comm_group(MPI_COMM_WORLD, group, err)
    call MPI_Group_size(group, group_size, err)
    call MPI_Group_incl(group, siz/2 , rank_list, new_group, err ) 
    call MPI_Comm_create(MPI_COMM_WORLD, new_group, new_comm, err)

    call MPI_Barrier(MPI_COMM_WORLD, err)
    if (rank == 0) then
        info = 42
    endif

    print *, "rank = ", rank, "info = ", info

    call MPI_Bcast(info, count=1, datatype=MPI_INTEGER, root=0, comm=MPI_COMM_WORLD, ierror=err)
    print *, "rank = ", rank, "info = ", info

    if (mod(rank,2) == 0) then
        call MPI_Comm_rank(new_comm, new_rank, err)
        if (new_rank == 0) then
            info = 43
        endif

        call MPI_Bcast(info, count=1, datatype=MPI_INTEGER, root=0, comm=new_comm, ierror=err)
    endif

    call MPI_Barrier(MPI_COMM_WORLD, err)
    if (rank == 0) then
        print *, "--------- --------"
    endif
    call MPI_Barrier(MPI_COMM_WORLD, err)
    print *, "rank = ", rank, "info = ", info
    call MPI_Group_free(new_group,err)
    call MPI_Finalize(err)
end program

